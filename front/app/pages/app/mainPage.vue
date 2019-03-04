<template>
  <v-ons-page>
    <v-ons-pull-hook :action="reload" @changestate="state = $event.state">
      <span v-show="state === 'initial'">Pull to refresh</span>
      <span v-show="state === 'preaction'">Release</span>
      <span v-show="state === 'action'">Loading...</span>
    </v-ons-pull-hook>

    <div class="container">
      <el-card class="box-card">
        <div class="title">あなたの残高</div>
        <div class="price">
          {{ profile.balance }}
          <span class="yen">円</span>
        </div>
      </el-card>
    </div>
    <div class="transfer" v-show="false">
      <div class="buttons">
        <el-button icon="el-icon-download" circle></el-button>
        <p class="name">請求</p>
      </div>
      <div class="buttons">
        <el-button icon="el-icon-upload2" circle></el-button>
        <p class="name">送金</p>
      </div>
    </div>
    <div class="history">
      <div class="header">最近のお支払い</div>
      <el-card class="history-card">
        <div @click="pushDetail(0)">
          <div class="left">
            <img src="~/static/t-sweets.png" width="70px" height="70px">
          </div>
          <div class="center">
            <div class="date">{{ dateString }}</div>
            <div class="title">{{ topTitle }}に支払い</div>
            <div class="status">
              <div class="payment-success">支払い完了</div>
            </div>
          </div>
          <div class="right">{{ amounts }}円</div>
        </div>
      </el-card>
    </div>
  </v-ons-page>
</template>


<script>
import Cookie from "js-cookie";
import { mapState, mapMutations, mapActions } from "vuex";
import detailPage from "~/pages/app/receiptDetailPage";

export default {
  data() {
    return {
      state: "initial",
      menus: [
        {
          title: "あなたの残高"
        },
        {
          title: "レシート"
        },
        {
          title: "レシート"
        }
      ]
    };
  },
  methods: {
    async pushDetail(index) {
      await this.setDetailIndex(index);
      this.$emit("push-page", detailPage);
    },
    async reload(done) {
      this.loading = this.$loading({
        text: "Loading",
        lock: false
      });
      if ((await this.getProfile()) && (await this.getCheckoutList())) {
        if (done) done();
        this.loading.close();
      } else {
        this.$ons.notification.alert({
          title: "Error",
          message: "情報の取得に失敗しました"
        });
        this.loading.close();
      }
    },
    logout() {
      this.$ons.notification
        .confirm({
          title: "確認",
          message: "ログアウトしますか？"
        })
        .then(response => {
          this.setAuth(null);
          Cookie.remove("auth");
        });
    },
    ...mapActions(["getProfile"]),
    ...mapActions("app", ["getCheckoutList"]),
    ...mapMutations("app", ["setDetailIndex"])
  },
  computed: {
    topTitle() {
      return this.checkoutList.length > 0
        ? this.checkoutList[0].merchant.name
        : null;
    },
    dateString() {
      return this.checkoutList.length > 0
        ? $nuxt.dateFormat(
            new Date(this.checkoutList[0].created_time),
            "YYYY/MM/DD hh:mm"
          )
        : null;
    },
    amounts() {
      return this.checkoutList.length > 0 ? this.checkoutList[0].amount : null;
    },
    ...mapState(["profile"]),
    ...mapState("app", ["checkoutList"])
  },
  async mounted() {
    await this.reload();
  }
};
</script>

<style lang="scss" scoped>
.container {
  .box-card {
    width: 90vw;
    height: 53vw;
    margin: 20px auto;
    border-radius: 10px;
    .title {
      color: gray;
      font-size: 16px;
    }
    .price {
      font-size: 30px;
      line-height: 130px;
      .yen {
        font-size: 14px;
      }
    }
  }
}
.transfer {
  .buttons {
    display: inline-block;
    margin: auto 20px;
    .name {
      font-size: 12px;
      color: #666;
    }
  }
}
.history {
  margin-top: 50px; // transfer hidden
  .header {
    font-size: 14px;
    color: grey;
    text-align: left;
    margin: 5px 30px;
  }
  .history-card {
    width: 95vw;
    margin: 0 auto;
    border-radius: 5px;
    .left {
      display: inline-block;
      width: 70px;
      vertical-align: top;
    }
    .center {
      display: inline-block;
      width: calc((95vw - 10px * 2) * 0.5);
      height: 70px;
      vertical-align: top;
      .date {
        text-align: left;
        font-size: 10px;
        color: rgb(102, 102, 102);
        padding-left: 28px;
      }
      .title {
        font-size: 18px;
        margin: 2px auto;
        padding-left: 10px;
      }
      .status {
        font-size: 12px;
        padding: 5px 20px 5px 20px;
        .payment-success {
          color: white;
          width: 100px;
          background-color: rgb(53, 187, 0);
          border-radius: 20px;
        }
      }
    }
    .right {
      display: inline-block;
      width: calc((95vw - 10px * 2) * 0.25);
      text-align: right;
      vertical-align: bottom;
    }

    &::before,
    &::after {
      contain: " ";
      clear: both;
    }
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

<style lang="scss">
.history-card {
  .el-card__body {
    padding: 10px;
  }
}
</style>
