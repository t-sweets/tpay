<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="center">新しいカードの登録</div>
    </v-ons-toolbar>
    <div class="container">
      <el-card class="box-card">
        <div class="title">{{ form.name }}</div>
      </el-card>

      <v-ons-list>
        <v-ons-list-header>カード情報</v-ons-list-header>
        <v-ons-list-item modifier="longdivider">
          <div class="left">カード名</div>
          <div class="center">
            <el-input placeholder="カード名を入力" v-model="form.name"></el-input>
          </div>
        </v-ons-list-item>
        <v-ons-list-item modifier="longdivider">
          <div class="left">IDm</div>
          <div class="right">{{ maskedIDm }}</div>
        </v-ons-list-item>
      </v-ons-list>

      <div class="register-buttons">
        <el-button type="primary" @click="registerConfirm">登録</el-button>
        <br>
        <el-button type="text" @click="cancelRegisterConfirm">登録をキャンセルする</el-button>
      </div>
    </div>
  </v-ons-page>
</template>


<script>
import Cookie from "js-cookie";
import { mapState, mapMutations, mapActions } from "vuex";
import index from "~/pages/index";

export default {
  data() {
    return {
      form: {
        name: "新しいカード",
        image_id: 1
      }
    };
  },
  methods: {
    async registerConfirm() {
      this.$confirm("この情報で登録しますか？", "Warning", {
        confirmButtonText: "登録する",
        cancelButtonText: "キャンセル",
        type: "warning",
        beforeClose: async (action, instance, done) => {
          if (action === "confirm") {
            instance.confirmButtonLoading = true;
            instance.confirmButtonText = "Loading...";
            const responce = await this.registerIdm({ name: this.form.name });
            if (responce === true) {
              instance.confirmButtonLoading = false;
              done();
              this.$message({
                type: "success",
                message: "登録が完了しました",
                onClose: () => {
                  this.$router.push("/");
                  this.$emit("pop-page");
                }
              });
            } else {
              instance.confirmButtonLoading = false;
              done();
              let errorMessage = "登録に失敗しました";
              if (responce == "This card is already registered") {
                errorMessage = "このカードは既に登録されています";
              }
              this.$message({
                type: "error",
                message: errorMessage
              });
            }
          }
        }
      });
    },
    cancelRegisterConfirm() {
      this.$confirm("登録をキャンセルします。よろしいですか？", "Warning", {
        confirmButtonText: "キャンセル",
        cancelButtonText: "登録に戻る",
        type: "warning"
      }).then(async () => {
        await this.resetIdm();
        this.$router.push("/");
        this.$emit("pop-page");
      });
    },
    ...mapMutations("app/register-idm", ["resetIdm"]),
    ...mapActions("app/register-idm", ["registerIdm"])
  },
  computed: {
    maskedIDm() {
      return this.idm ? "************" + this.idm.slice(-4) : "";
    },
    ...mapState("app/register-idm", ["idm"])
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
      color: #666;
      font-size: 25px;
      line-height: 150px;
    }
  }
}
.register-buttons {
  margin: 50px auto;
  button {
    width: 75%;
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
