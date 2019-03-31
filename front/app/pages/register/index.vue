<template>
  <div class="container">
    <el-card class="box-card login">
      <div slot="header" class="clearfix">
        <span>Register</span>
      </div>

      <el-form
        ref="registerForm"
        :model="form"
        :rules="rules"
        :label-position="labelPosition"
        label-width="180px"
        @submit.native.prevent="onSubmit"
      >
        <el-form-item label="Name" prop="name" required>
          <el-input v-model="form.name" placeholder="tagokentarou"></el-input>
        </el-form-item>
        <el-form-item label="Email" prop="email" required>
          <el-input type="email" v-model="form.email" placeholder="hogehoge@example.com"></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password" required>
          <el-input v-model="form.password" placeholder="password" autocomplete="off" show-password></el-input>
        </el-form-item>
        <el-form-item label="Nickname" prop="nickname" required>
          <el-input type="text" v-model="form.nickname" placeholder="田胡研"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit">Register</el-button>
          <el-button type="text" @click="$router.push('login')">Login</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      isRegister: false,
      form: {
        name: null,
        email: null,
        password: null,
        nickname: null
      },
      rules: {
        name: [
          {
            required: true,
            message: "LDAP名を入力してください",
            trigger: "blur"
          },
          {
            min: 3,
            max: 10,
            message: "LDAP名は３文字以上10文字以内で入力してください",
            trigger: "blur"
          }
        ],
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
        ],
        password: [
          {
            required: true,
            message: "パスワードを入力してください",
            trigger: "blur"
          }
        ],
        nickname: [
          {
            required: true,
            message: "ニックネームを入力してください",
            trigger: "blur"
          },
          {
            min: 3,
            max: 10,
            message: "ニックネームは３文字以上10文字以内で入力してください",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    async onSubmit() {
      await this.$refs.registerForm.validate(async valid => {
        if (valid) {
          if (
            await this.register({
              username: this.form.name,
              email: this.form.email,
              display_name: this.form.nickname,
              password: this.form.password
            })
          ) {
            this.$alert("ユーザー登録が完了しました", "登録完了", {
              type: "success",
              confirmButtonText: "OK",
              callback: action => {
                this.$router.push("/");
              }
            });
          } else {
            this.$message({
              type: "error",
              message: "登録に失敗しました"
            });
          }
        } else {
          this.$message({
            type: "error",
            message: "必要項目を入力してください"
          });
        }
      });
    },
    ...mapActions(["register"])
  },
  computed: {
    labelPosition() {
      return window.matchMedia("(max-width:1024px)").matches ? "top" : "left";
    }
  },
  layout: "default"
};
</script>

<style lang="scss" scoped>
.container {
  .login {
    @include pc {
      width: 80%;
    }
    @include sp {
      width: 100%;
    }
    margin: 0 auto;
  }
  form {
    @include pc {
      margin: 20px 50px;
    }
    @include sp {
      margin: 0;
    }
  }
}
</style>
