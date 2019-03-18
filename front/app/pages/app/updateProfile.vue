<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">プロフィール変更</div>
    </v-ons-toolbar>

    <el-form ref="updateProfileForm" :model="form" label-width="120px" :rules="rules" @submit.native.prevent="onSubmit">
      <div class="user-data">
        <div class="userimage">
        </div>
      </div>
      <el-form-item label="display name" prop="display name">
        <el-input type="text" v-model="form.display_name"></el-input>
      </el-form-item>
      <el-form-item label="email" required prop="email">
        <el-input type="email" v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" native-type="submit"> Update </el-button>
      </el-form-item>
    </el-form>

  </v-ons-page>
</template>

<script>
import {mapState, mapActions} from "vuex"
export default {
  computed: {
    ...mapState(["profile"]),
  },
  data() {
      return {
        form: {
          display_name: '',
          email: ''
        },
        rules: {
          email: [
            {
              required: true,
              message: "メールアドレスを入力してください",
              trigger: "blur"
            },
            {
              type: "email",
              message: "有効なメールアドレスを入力してください",
              trigger: ["blur", "change"]
            }
          ]
        }
      }
  },
  methods: {
      async onSubmit() {
          await this.$refs.updateProfileForm.validate(async valid => {
              if (valid) {
                  if (
                    await this.updateProfile({
                      display_name: this.form.display_name,
                      email: this.form.email
                    })
                  ) {
                      this.$message({message: "プロフィールを更新しました", type: "success"});
                      this.$emit("pop-page");
                  } else {
                      this.$message({message: "プロフィールを更新できませんでした", type: "error"});
                  }
              }
          });
      },
      ...mapActions(["updateProfile"])
  },
  mounted() {
    this.form.display_name = this.profile.display_name
    this.form.email = this.profile.email
  }
}

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
}
</style>
