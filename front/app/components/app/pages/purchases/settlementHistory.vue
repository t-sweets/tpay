<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button/>
      </div>
      <div class="center">決済履歴</div>
    </v-ons-toolbar>
    <div class="settlement-list">
      <el-card class="receipt-card" v-for="(item, index) in transactionList" :key="item.id">
        <div @click="pushDetail(index)">
          <div class="header">
            <div class="left">決済番号&nbsp;{{item.id}}</div>
            <div class="right">{{ toDateString(item.created_time) }}</div>
          </div>
          <div class="left">
            <img :src="storeIcon(item.merchant.icon)" alt width="50px" height="50px">
          </div>
          <div class="center">
            <div class="title">{{ titleStr(item) }}</div>
            <div class="status">
              <div :class="toClassStr(item)">{{ toStatusStr(item) }}</div>
            </div>
          </div>
          <div class="right">{{ item.amount }}円</div>
        </div>
      </el-card>
    </div>
  </v-ons-page>
</template>

<script>
import { mapActions, mapState, mapMutations } from "vuex";
import detailPage from "~/components/app/pages/purchases/receiptDetailPage";
export default {
  methods: {
    storeIcon(url) {
      return url
        ? process.env.API_HOST + "/../.." + url.image
        : require("~/assets/images/icons/shop-noimage.svg");
    },
    toDateString(date) {
      return $nuxt.dateFormat(new Date(date), "YYYY/MM/DD hh:mm");
    },
    toStatusStr(item) {
      switch (item.type) {
        case "checkout":
          return item.deleted
            ? "キャンセル済"
            : item.amount >= 0
            ? "返金完了"
            : "支払い完了";
          break;
        case "deposit":
          return "チャージ完了";
      }
    },
    toClassStr(item) {
      switch (item.type) {
        case "checkout":
          if (item.deleted) return "canceled";
          else if (item.amount >= 0) return "refunded";
        case "deposit":
        default:
          return item.type;
      }
      if (item.type == "checkout") {
      }
      return item.type == "checkout" && item.deleted ? "refunded" : item.type;
    },
    titleStr(item) {
      switch (item.type) {
        case "checkout":
          if (item.deleted)
            return `${item.merchant.name || "お店"}への支払いをキャンセル`;
          else if (item.amount >= 0)
            return `${item.merchant.name || "お店"}からの返金`;
          else return `${item.merchant.name || "お店"}への支払い`;
        case "deposit":
          return `${item.merchant.name || "お店"}でチャージ`;
      }
    },
    async pushDetail(index) {
      await this.setDetailIndex(index);
      this.$emit("push-page", detailPage);
    },
    ...mapActions("app", ["setDetailIndex", "getTransaction"]),
    ...mapMutations("app", ["setDetailIndex"])
  },
  computed: {
    ...mapState("app", ["transactionList"])
  },
  async mounted() {
    await this.getTransaction();
  }
};
</script>

<style lang="scss" scoped>
.settlement-list {
  -webkit-overflow-scrolling: touch;
  overflow-scrolling: touch;
  .receipt-card {
    width: 95vw;
    margin: 10px auto;
    border-radius: 5px;
    .header {
      color: #666;
      border-bottom: 1px solid #ddd;
      padding-bottom: 2px;
      margin-bottom: 5px;
      .left {
        display: inline-block;
        text-align: left;
        vertical-align: bottom;
        width: 65%;
        height: 15px;
        font-size: 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
      }
      .right {
        display: inline-block;
        text-align: right;
        vertical-align: bottom;
        width: 30%;
        height: 15px;
        font-size: 12px;
      }
    }
    .left {
      display: inline-block;
      width: 50px;
      height: 50px;
      vertical-align: top;
      img {
        border-radius: 100%;
      }
    }
    .center {
      display: inline-block;
      width: calc((95vw - 10px * 2) * 0.5);
      height: 50px;
      vertical-align: top;
      .date {
        font-size: 15px;
        color: rgb(102, 102, 102);
      }
      .title {
        text-align: left;
        font-size: 12px;
        margin: 5px auto;
        padding-left: 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
      }
      .status {
        font-size: 10px;
        padding: 2px 10px 2px 10px;
        font-weight: 600;
        .checkout {
          color: white;
          width: 70px;
          background-color: rgb(53, 187, 0);
          border-radius: 20px;
        }
        .deposit {
          color: white;
          width: 70px;
          background-color: rgb(0, 140, 255);
          border-radius: 20px;
        }
        .canceled {
          color: white;
          width: 70px;
          background-color: rgb(124, 124, 124);
          border-radius: 20px;
        }
        .refunded {
          color: white;
          width: 70px;
          background-color: rgb(255, 152, 34);
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
</style>

<style lang="scss">
.receipt-card {
  .el-card__body {
    padding: 0px 0px 5px 0px !important;
  }
}
</style>
