<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">詳細</div>
    </v-ons-toolbar>

    <div class="detail-page">
      <div class="detail-body">
        <div class="store-icon">
          <img :src="storeIcon(getDetail.merchant.icon)" alt width="100px" height="100px">
        </div>
        <div class="store-name">{{ getDetail.merchant.name }}に支払い</div>
        <div class="payment-time">{{ paymentTime }}</div>
        <div class="payment-price">
          <span class="price">{{ getDetail.amount }}</span>
          <span class="yen">円</span>
        </div>
        <div class="status">
          <div class="payment-success">支払い完了</div>
        </div>
        <hr>
        <div class="details">
          <div class="detail">
            <div class="left">店舗名</div>
            <div class="right">{{ getDetail.merchant.name }}</div>
          </div>
          <div class="detail">
            <div class="left">決済番号</div>
            <div class="right" style="font-size: 10px;">{{ getDetail.id }}</div>
          </div>
          <div class="detail">
            <div class="left">支払い金額</div>
            <div class="right" style="font-weight: bold;">{{ getDetail.amount }}円</div>
          </div>
        </div>
      </div>
    </div>
  </v-ons-page>
</template>

<script>
import { mapState, mapGetters } from "vuex";
export default {
  methods: {
    storeIcon(url) {
      return url ? url : require("~/assets/images/icons/shop-noimage.svg");
    }
  },
  computed: {
    paymentTime() {
      return $nuxt.dateFormat(
        new Date(this.getDetail.created_time),
        "YYYY年MM月DD日(E) hh:mm"
      );
    },
    ...mapGetters("app", ["getDetail"])
  },
  mounted() {
    if (this.getDetail.length < 1) {
      this.$ons.notification.alert("エラーが発生しました");
    }
  }
};
</script>


<style lang="scss" scoped>
.detail-page {
  padding-top: 30px;
  //   background: linear-gradient(
  //     130deg,
  //     rgba(0, 54, 255, 1) 0%,
  //     rgba(0, 212, 255, 1) 35%,
  //     rgba(255, 255, 255, 1) 100%
  //   );
  height: 100%;
  .detail-body {
    width: 95vw;
    background-color: white;
    margin: 0 auto;
    margin-top: 30px;
    border-radius: 5px;
    box-shadow: 10px #000;
    .store-icon {
      width: 110px;
      height: 110px;
      background-color: white;
      border: 1px solid #ddd;
      border-radius: 100%;
      margin-top: -50px;
      margin-left: calc(50vw - (110px + 5vw) / 2);
      position: absolute;
      img {
        margin: 4px 5px 5px 4px;
      }
    }
    .store-name {
      padding-top: 70px;
      font-size: 20px;
      font-weight: 400;
    }
    .payment-time {
      color: #666;
      font-size: 14px;
      margin: 5px;
    }
    .payment-price {
      margin-top: 18px;
      padding-left: 20px;
      .price {
        font-size: 40px;
        font-weight: bold;
        letter-spacing: 0.05em;
      }
      .yen {
        font-size: 18px;
      }
    }
    .status {
      font-size: 13px;
      margin-bottom: 25px;
      .payment-success {
        color: white;
        width: 100px;
        margin: 10px auto;
        background-color: rgb(53, 187, 0);
        border-radius: 20px;
      }
    }
    hr {
      background-color: #ddd;
      height: 1px;
      border: 0;
    }
    .details {
      font-size: 12px;
      padding-bottom: 30px;
      .detail {
        color: #444;
        .left {
          display: inline-block;
          width: 35%;
          text-align: left;
          padding-left: 25px;
          padding-right: 25px;
        }
        .right {
          display: inline-block;
          width: 60%;
          text-align: right;
          padding-left: 25px;
          padding-right: 25px;
        }
      }
    }
  }
}
</style>

