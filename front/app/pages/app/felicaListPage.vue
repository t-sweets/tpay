<template>
  <v-ons-page id="felicaListPage">
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">Felicaカード管理</div>
    </v-ons-toolbar>

    <div>
      <v-ons-carousel swipeable overscrollable auto-scroll :index.sync="cardIndex">
        <v-ons-carousel-item v-for="item in felicaList" :key="item.id">
          <el-card class="box-card">
            <div class="title"></div>
            <div class="price">{{ item.name }}</div>
          </el-card>
        </v-ons-carousel-item>
      </v-ons-carousel>
      <div class="dots">
        <span
          v-for="(item, index) in felicaList"
          :key="item.id"
          style="cursor: pointer"
          @click="cardIndex = index"
        >{{ cardIndex === index ? '\u25CF' : '\u25CB' }}</span>
      </div>
    </div>

    <v-ons-list>
      <v-ons-list-item modifier="longdivider">
        <div class="left">カード名</div>
        <div class="center">{{ cardList[cardIndex].name }}</div>
      </v-ons-list-item>
      <v-ons-list-item modifier="longdivider">
        <div class="left">IDm</div>
        <div class="center">{{ cardList[cardIndex].idm }}</div>
      </v-ons-list-item>
      <v-ons-list-item modifier="longdivider">
        <div class="left">最終利用日</div>
        <div class="center">{{ cardList[cardIndex].lastDate }}</div>
      </v-ons-list-item>
    </v-ons-list>
    <br>
    <v-ons-list>
      <v-ons-list-item tappable>
        <div class="center">
          <span style="color:red; margin:0 auto;">削除</span>
        </div>
      </v-ons-list-item>
    </v-ons-list>
  </v-ons-page>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {
      cardIndex: 0,
      cardList: [
        {
          name: "学生証",
          idm: "aaaaaa",
          lastDate: "2019-12-02 10:00:00"
        },
        {
          name: "Suica",
          idm: "aaaaaa",
          lastDate: "2019-12-01 10:00:00"
        }
      ]
    };
  },
  methods: {
    ...mapActions("app", ["getFelicaList"])
  },
  computed: {
    ...mapState("app", ["felicaList"])
  },
  async mounted() {
    if (await this.getFelicaList()) {
    } else {
      this.$ons.notification.alert("エラーが発生しました");
    }
  }
};
</script>

<style lang="scss">
#felicaListPage {
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
      font-size: 20px;
      line-height: 130px;
    }
  }

  .dots {
    text-align: center;
    font-size: 30px;
    color: #666;
  }
  ons-list-item {
    color: #666;
    .list-item__left {
      width: 30%;
    }
  }
}
</style>
