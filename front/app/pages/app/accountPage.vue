<template>
  <v-ons-page>
    <div class="user-data">
      <div class="userimage"></div>
      <div class="user-name">{{ displayName }}</div>
    </div>
    <el-row class="menus" :gutter="0">
      <el-col v-for="menu in menus" :key="menu.id" :span="8" :offset="0">
        <div class="menu-item" @click="$emit('push-page', menu.page)">
          <div class="item-icon"></div>
          <div class="item-name">{{ menu.title }}</div>
        </div>
      </el-col>
    </el-row>
    <v-ons-list>
      <v-ons-list-header></v-ons-list-header>
      <v-ons-list-item modifier="chevron" tappable @click="pushFelicaPage">Felicaカードの管理</v-ons-list-item>
      <v-ons-list-item modifier="chevron" tappable @click="logout">
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

export default {
  data() {
    return {
      menus: [
        {
          title: "あなたの残高",
          page: settlementHistory
        },
        {
          title: "レシート",
          page: receiptPage
        },
        {
          title: "レシート"
        }
      ]
    };
  },
  methods: {
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
</style>
