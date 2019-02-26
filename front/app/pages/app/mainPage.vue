<template>
  <v-ons-page>
    <div class="container">
      <el-card class="box-card">
        <div class="title">あなたの残高</div>
        <div class="price">
          10,000
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
        <div class="left">
          <div style="background-color:red;width:70px; height:70px;"></div>
        </div>
        <div class="center">
          <div class="date">2019年2月26日 11時17分</div>
          <div class="title">Sweetsに支払い</div>
          <div class="status">
            <div class="payment-success">支払い完了</div>
          </div>
        </div>
        <div class="right">300円</div>
      </el-card>
    </div>
  </v-ons-page>
</template>


<script>
import Cookie from "js-cookie";
import { mapState, mapMutations } from "vuex";

export default {
  data() {
    return {
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
    logout() {
      this.$ons.notification
        .confirm({
          title: "確認",
          message: "ログアウトしますか？"
        })
        .then(response => {
          //   this.setAuth(null);
          //   Cookie.remove("auth");
        });
    }
  },
  computed: {
    // ...mapState(["profile"])
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
      width: calc((95vw - 10px * 2) * 0.45);
      height: 70px;
      vertical-align: top;
      .date {
        font-size: 10px;
        color: rgb(102, 102, 102);
      }
      .title {
        font-size: 18px;
        margin: 2px auto;
      }
      .status {
        font-size: 12px;
        padding: 5px 20px;
        .payment-success {
          color: white;
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
