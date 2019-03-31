<template>
  <v-ons-page>
    <div class="user-data">
      <div class="userimage"></div>
      <div class="user-name">{{ displayName }}</div>
    </div>
    <el-row class="menus" :gutter="0">
      <el-col v-for="menu in menus" :key="menu.id" :span="8" :offset="0">
        <div class="menu-item" @click="pushButton(menu)">
          <div class="item-icon">
            <font-awesome-icon
              v-if="typeof menu.icon == 'object'"
              class="card-icon"
              :icon="menu.icon"
            />
            <img
              style="margin-top:20px"
              v-if="typeof menu.icon === 'string'"
              :src="menu.icon"
              width="50"
              height="50"
            >
          </div>
          <div class="item-name">{{ menu.title }}</div>
        </div>
      </el-col>
    </el-row>
    <v-ons-list class="accounts-menu">
      <v-ons-list-item modifier="chevron nodivider" tappable @click="pushFelicaPage">Felicaカードの管理</v-ons-list-item>
      <v-ons-list-item modifier="chevron nodivider" tappable @click="pushPassChangePage">パスワード変更</v-ons-list-item>
      <v-ons-list-item modifier="chevron nodivider" tappable @click="logout">
        <span style="color:red;">ログアウト</span>
      </v-ons-list-item>
    </v-ons-list>
  </v-ons-page>
</template>

<script>
import Cookie from "js-cookie";
import { mapMutations, mapState } from "vuex";

import felicaListPage from "~/pages/app/felicaListPage";
import receiptPage from "~/pages/app/receiptPage";
import settlementHistory from "~/pages/app/settlementHistory";
import changePassword from "@/components/app/pages/passwordChangePage";

export default {
  data() {
    return {
      menus: [
        {
          title: "レシート",
          icon: require("~/assets/images/icons/receipt.svg"),
          page: receiptPage
        },
        {
          title: "決済履歴",
          icon: require("~/assets/images/icons/wallet.svg"),
          page: settlementHistory
        },
        {
          title: "個人間送金",
          icon: require("~/assets/images/icons/sendmoney.svg"),
          click: () => {
            this.$alert(
              "準備中です。もうしばらくお待ちください",
              "Comming Soon!",
              {
                confirmButtonText: "OK"
              }
            );
          }
        }
      ]
    };
  },
  methods: {
    pushButton(menu) {
      if (menu.page) {
        this.$emit("push-page", menu.page);
      } else if (menu.click) {
        menu.click();
      }
    },
    logout() {
      this.$ons.notification
        .confirm({
          title: "確認",
          message: "ログアウトしますか？"
        })
        .then(index => {
          if (index == 1) {
            this.setAuth(null);
            Cookie.remove("auth");
            this.$router.push("/login");
          }
        });
    },
    pushFelicaPage() {
      this.$emit("push-page", felicaListPage);
    },
    pushPassChangePage() {
      this.$emit("push-page", {
        extends: changePassword,
        onsNavigatorOptions: {
          animation: "lift",
          animationOptions: { duration: 0.5 }
        }
      });
    },
    ...mapMutations(["setAuth"])
  },
  computed: {
    displayName() {
      return this.profile.display_name
        ? this.profile.display_name
        : this.profile.username;
    },
    ...mapState(["profile"])
  }
};
</script>



<style lang="scss" scoped>
.user-data {
  padding-top: 50px;
  padding-bottom: 10px;
  background-color: white;
  .userimage {
    width: 100px;
    height: 100px;
    border-radius: 100%;
    margin: 0 auto;
    background: gray;
  }
  .user-name {
    margin: 10px;
    font-size: 20px;
    font-weight: 800;
  }
}
.menus {
  background-color: white;
  padding-top: 10px;

  padding-bottom: 20px;
  .menu-item {
    &:nth-child(2n) {
      border-left: 1px solid #777;
      border-right: 1px solid #777;
    }
    .item-icon {
      width: 100%;
      height: 80px;
      margin: 0 auto;
    }
    &:active {
      background: #ddd;
    }
  }
}
.accounts-menu {
  margin-top: 20px;
  background-image: none;
}
</style>
