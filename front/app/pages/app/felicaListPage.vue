<template>
  <v-ons-page id="felicaListPage">
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">Felicaカード管理</div>
      <div class="right">
        <v-ons-toolbar-button @click="pushQRReaderPage">
          <i class="el-icon-circle-plus-outline"></i>
        </v-ons-toolbar-button>
      </div>
    </v-ons-toolbar>

    <div>
      <v-ons-carousel
        swipeable
        overscrollable
        auto-scroll
        :index.sync="cardIndex"
        v-if="felicaList.length > 0"
      >
        <v-ons-carousel-item v-for="item in showFelicLists" :key="item.id">
          <el-card class="box-card">
            <div class="title"></div>
            <div class="price">{{ item.name }}</div>
          </el-card>
        </v-ons-carousel-item>
      </v-ons-carousel>

      <el-card v-else class="box-card">
        <div class="title"></div>
        <div class="no-registed">カードが登録されていません</div>
      </el-card>

      <div class="dots">
        <span
          v-for="(item, index) in showFelicLists"
          :key="item.id"
          style="cursor: pointer"
          @click="cardIndex = index"
        >{{ cardIndex === index ? '\u25CF' : '\u25CB' }}</span>
      </div>
    </div>

    <v-ons-list>
      <v-ons-list-item modifier="longdivider">
        <div class="left">カード名</div>
        <div class="center">{{ showFelicLists[cardIndex].name }}</div>
      </v-ons-list-item>
      <v-ons-list-item modifier="longdivider">
        <div class="left">IDm</div>
        <div class="center">{{ showFelicLists[cardIndex].idm }}</div>
      </v-ons-list-item>
    </v-ons-list>
    <br>
    <v-ons-list v-show="showFelicLists[0].name != ''">
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
import qrReaderPage from "~/pages/app/qrReaderPage";
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
    pushQRReaderPage() {
      this.$emit("push-page", qrReaderPage);
    },
    ...mapActions("app", ["getFelicaList"])
  },
  computed: {
    showFelicLists() {
      return this.felicaList.length > 0
        ? this.felicaList
        : [{ name: "", idm: "" }];
    },
    ...mapState("app", ["felicaList"])
  },
  async created() {
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
    .no-registed {
      color: #666;
      font-size: 15px;
      line-height: 150px;
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
