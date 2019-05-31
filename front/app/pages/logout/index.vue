<template>
  <div class="container">
    <el-card class="box-card login">
      <div slot="header" class="clearfix">
        <span>Logout</span>
      </div>
      <p>ログアウトしました</p>
      <el-button type="text" @click="$router.push('/login')">再度ログインする</el-button>
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
    ...mapActions(["login"])
  },
  computed: {
    labelPosition() {
      return window.matchMedia("(max-width:1024px)").matches ? "top" : "left";
    },
    ...mapState(["auth"])
  },
  created() {}
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

