<template>
  <div class="container">
    <el-card class="box-card login">
      <div slot="header" class="clearfix">
        <span>Login</span>
        <el-button style="float: right; padding: 3px 0" type="text">Forget password</el-button>
      </div>

      <el-form ref="form" :model="form" :label-position="labelPosition" label-width="180px">
        <el-form-item label="Name">
          <el-input type="text" v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Login</el-button>
          <el-button type="text" @click="$router.push('register')">Regiter</el-button>
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
      }
    };
  },
  methods: {
    async onSubmit() {
      if (
        await this.login({
          username: this.form.name,
          password: this.form.password
        })
      ) {
        Cookie.set("auth", this.auth.Authorization, { expires: 3 });
        this.$router.push("/");
      } else {
        this.$alert("このユーザー名・パスワードは無効です", "認証エラー", {
          type: "error",
          confirmButtonText: "OK"
        });
      }
    },
    ...mapActions(["login", "getProfile"])
  },
  computed: {
    labelPosition() {
      return window.matchMedia("(max-width:1024px)").matches ? "top" : "left";
    },
    ...mapState(["auth", "profile"])
  }
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

