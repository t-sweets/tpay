<template>
  <div class="container">
    <el-card class="box-card login">
      <div slot="header" class="clearfix">
        <span>Login</span>
        <el-button style="float: right; padding: 3px 0" type="text">Forget password</el-button>
      </div>

      <el-form
        ref="loginForm"
        :model="form"
        :label-position="labelPosition"
        label-width="180px"
        :rules="rules"
        @submit.native.prevent="onSubmit"
      >
        <el-form-item label="Name" prop="name">
          <el-input type="text" v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit">Login</el-button>
          <el-button type="text" @click="$router.push('/register/')">Regiter</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import Cookie from "js-cookie";

export default {
  data() {
    return {
      isRegister: false,
      form: {
        name: null,
        password: null
      },
      rules: {
        name: [
          {
            required: true,
            message: "LDAP名を入力してください",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            message: "パスワードを入力してください",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    async onSubmit() {
      await this.$refs.loginForm.validate(async valid => {
        if (valid) {
          const res = await this.login({
            username: this.form.name,
            password: this.form.password
          });
          if (res === true) {
            Cookie.set("auth", this.auth.Authorization, { expires: 3 });
            this.$route.params
              ? this.$router.push("/")
              : this.$router.push("/");
          } else {
            this.$alert(this.$nuxt.err_message(res), "認証エラー", {
              type: "error",
              confirmButtonText: "OK"
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
    ...mapActions(["login", "getProfile"])
  },
  computed: {
    labelPosition() {
      return window.matchMedia("(max-width:1024px)").matches ? "top" : "left";
    },
    ...mapState(["auth", "profile"])
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

