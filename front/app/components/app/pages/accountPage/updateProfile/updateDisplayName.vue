<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">ユーザー名</div>
    </v-ons-toolbar>

    <div class="background"></div>

    <el-form
      class="updateForm"
      ref="updateProfileForm"
      :model="form"
      :rules="rules"
      @submit.native.prevent="onSubmit"
    >
      <el-form-item prop="display_name">
        <el-input type="text" v-model="form.display_name" clearable></el-input>
      </el-form-item>
      <el-form-item>
        <el-button round type="primary" native-type="submit">変更を保存</el-button>
      </el-form-item>
    </el-form>
  </v-ons-page>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: {
    ...mapState(["profile"])
  },
  data() {
    return {
      form: {
        display_name: "",
        email: ""
      },
      rules: {
        display_name: [
          {
            required: true,
            message: "ユーザー名を入力してください（ユーザー名は公開されます）",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    async onSubmit() {
      await this.$refs.updateProfileForm.validate(async valid => {
        if (valid) {
          const loading = this.$loading({
            lock: true
          });
          if (
            await this.updateProfile({
              display_name: this.form.display_name
            })
          ) {
            loading.close();
            this.$message({
              message: "プロフィールを更新しました",
              type: "success"
            });
            this.$emit("pop-page");
          } else {
            loading.close();
            this.$message({
              message: "プロフィールを更新できませんでした",
              type: "error"
            });
          }
        }
      });
    },
    ...mapActions(["updateProfile"])
  },
  mounted() {
    this.form.display_name = this.profile.display_name;
  }
};
</script>

<style lang="scss" scoped>
.updateForm {
  margin: 20px 10px;
  button {
    font-weight: bold;
    width: 80%;
  }
}
.background {
  background-color: white;
  background-image: none;
}
</style>
