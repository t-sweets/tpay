<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">レシート</div>
    </v-ons-toolbar>

    <div>
      <el-card class="receipt-card" v-for="(item, index) in checkoutList" :key="item.id">
        <div @click="pushDetail(index)">
          <div class="header">
            <div class="left">決済番号&nbsp;{{item.id}}</div>
            <div class="right">{{ toDateString(item.created_time) }}</div>
          </div>
          <div class="left">
            <img src="~/static/t-sweets.png" alt width="50px" height="50px">
          </div>
          <div class="center">
            <div class="title">{{ item.merchant }}に支払い</div>
            <div class="status">
              <div class="payment-success">支払い完了</div>
            </div>
          </div>
          <div class="right">{{ item.amount }}円</div>
        </div>
      </el-card>
    </div>
  </v-ons-page>
</template>

<script>
import { mapState, mapActions, mapMutations } from "vuex";
import detailPage from "~/pages/app/receiptDetailPage";

export default {
  data() {
    return {};
  },
  methods: {
    toDateString(date) {
      return $nuxt.dateFormat(new Date(date), "YYYY/MM/DD hh:mm");
    },
    async pushDetail(index) {
      await this.setDetailIndex(index);
      this.$emit("push-page", detailPage);
    },
    ...mapActions("app", ["getCheckoutList"]),
    ...mapMutations("app", ["setDetailIndex"])
  },
  computed: {
    ...mapState("app", ["checkoutList"])
  },
  async mounted() {
    if (await this.getCheckoutList()) {
    } else {
    }
  }
};
</script>

<style lang="scss" scoped>
.receipt-card {
  width: 95vw;
  margin: 10px auto;
  border-radius: 5px;
  .header {
    color: #666;
    border-bottom: 1px solid #ddd;
    .left {
      display: inline-block;
      text-align: left;
      vertical-align: bottom;
      width: 220px;
      height: 15px;
      font-size: 3px;
    }
    .right {
      display: inline-block;
      text-align: right;
      vertical-align: bottom;
      width: 80px;
      height: 15px;
      font-size: 10px;
    }
  }
  .left {
    display: inline-block;
    width: 50px;
    height: 50px;
    vertical-align: top;
  }
  .center {
    display: inline-block;
    width: calc((95vw - 10px * 2) * 0.5);
    height: 50px;
    vertical-align: top;
    .date {
      font-size: 10px;
      color: rgb(102, 102, 102);
    }
    .title {
      text-align: left;
      font-size: 12px;
      margin: 5px auto;
      padding-left: 10px;
    }
    .status {
      font-size: 10px;
      padding: 2px 10px 2px 10px;
      .payment-success {
        color: white;
        width: 70px;
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
</style>

<style lang="scss">
.receipt-card {
  .el-card__body {
    padding: 0px 5px !important;
  }
}
</style>