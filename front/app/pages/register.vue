<template>
  <div class="container">
    <el-card class="box-card login">
      <div slot="header" class="clearfix">
        <span>Register</span>
      </div>

      <el-form ref="form" :model="form" :label-position="labelPosition" label-width="180px">
        <el-form-item label="Name" required>
          <el-input v-model="form.name" placeholder="tagokentarou"></el-input>
        </el-form-item>
        <el-form-item label="Email" required>
          <el-input type="email" v-model="form.email" placeholder="hogehoge@example.com"></el-input>
        </el-form-item>
        <el-form-item label="Password" required>
          <el-input type="password" v-model="form.password" placeholder="password"></el-input>
        </el-form-item>
        <el-form-item label="Nickname" required>
          <el-input type="text" v-model="form.nickname" placeholder="田胡研"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Register</el-button>
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
      }
    };
  },
  methods: {
    async onSubmit() {
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
      }
    },
    ...mapActions(["register"])
  },
  computed: {
    labelPosition() {
      return window.matchMedia("(max-width:1024px)").matches ? "top" : "left";
    }
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
