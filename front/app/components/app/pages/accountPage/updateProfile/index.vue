<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">アカウント設定</div>
    </v-ons-toolbar>

    <div class="profiles">
      <div class="profile-header">プロフィール</div>
      <div class="user-data">
        <el-upload
          class="profile-image-uploader"
          action="#"
          :show-file-list="false"
          :on-change="submitIcon"
        >
          <img
            v-if="profile.icon != null && profile.icon.image != null"
            :src="iconURL"
            class="product-image"
          >
          <i v-else class="el-icon-plus product-image-uploader-icon"></i>
        </el-upload>
      </div>
    </div>

    <v-ons-list>
      <v-ons-list-item tappable @click="openEditDisplayName">
        <div class="left">ユーザー名</div>
        <div class="center"></div>
        <div class="right">{{ profile.display_name }}</div>
      </v-ons-list-item>
      <v-ons-list-item v-if="false">
        <div class="center">検索画面での表示</div>
        <div class="right">
          <el-switch v-model="value2"></el-switch>
        </div>
      </v-ons-list-item>
    </v-ons-list>
    <div class="list-hr">
      <hr size="0.5" color="#ddd" noshade>
    </div>
    <v-ons-list>
      <div class="ons-list-header">アカウント情報</div>
      <v-ons-list-item tappable @click="alertCannotEdit('LDAP名')">
        <div class="left">LDAP名</div>
        <div class="center"></div>
        <div class="right">{{ profile.username }}</div>
      </v-ons-list-item>
      <v-ons-list-item tappable @click="openEditEmail">
        <div class="left">メールアドレス</div>
        <div class="center"></div>
        <div class="right">{{ profile.email }}</div>
      </v-ons-list-item>
    </v-ons-list>
  </v-ons-page>
</template>

<script>
import { mapState, mapActions } from "vuex";
import updateDisplayName from "@/components/app/pages/accountPage/updateProfile/updateDisplayName";
import updateEmail from "@/components/app/pages/accountPage/updateProfile/updateEmail";

export default {
  data() {
    return {
      form: {
        icon: null
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
    };
  },
  methods: {
    openEditDisplayName() {
      this.$emit("push-page", updateDisplayName);
    },
    openEditEmail() {
      this.$emit("push-page", updateEmail);
    },
    alertCannotEdit(name) {
      this.$ons.notification.alert({
        title: "変更できません",
        message: `${name}は変更できません。\n変更される場合は、システム管理者までお問い合わせください。`
      });
    },
    async submitIcon() {
      var params = new FormData();
      const fileDom = document.querySelector("[name='file']");
      if (!fileDom.files[0]) return false;
      const loading = this.$loading({
        lock: true
      });
      params.append("image", fileDom.files[0]);
      if (await this.uploadIcon(params)) {
        loading.close();
        this.$message({
          message: "プロフィール画像を更新しました",
          type: "success"
        });
      } else {
        loading.close();
        this.$message({
          message: "プロフィール画像を更新できませんでした",
          type: "error"
        });
      }
    },
    ...mapActions(["uploadIcon"])
  },
  computed: {
    uploadURL() {
      return `${process.env.API_HOST}/media/upload/`;
    },
    iconURL() {
      return this.profile.icon.image
        ? this.profile.icon.image
        : require("@/assets/images/icons/guest_icon.svg");
    },
    ...mapState(["profile"])
  }
};
</script>

<style lang="scss" scoped>
.profiles {
  margin-bottom: 20px;
  .profile-header {
    color: gray;
    font-size: 12px;
    margin: 5px 10px;
    text-align: left;
  }
  .user-data {
    padding-bottom: 10px;
    background-color: white;
    .userimage {
      width: 80px;
      height: 80px;
      border-radius: 100%;
      margin: 0 auto;
      background: gray;
    }
  }
}
.list-hr {
  padding: 10px 0;
  background-color: white;
}
ons-list {
  .ons-list-header {
    color: gray;
    font-size: 12px;
    margin: 0px 10px;
    text-align: left;
  }
  &.list {
    background-image: none !important;
  }
  ons-list-item {
    div {
      background-image: none !important;
      &.left,
      &.center {
        color: #444;
      }
      &.right {
        color: #0597d1;
      }
    }
  }
}
</style>


<style lang="scss">
.profiles {
  .user-data {
    .profile-image-uploader {
      .el-upload {
        border: 1px dashed #0597d1;
        border-radius: 100%;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        &:hover {
          border-color: #409eff;
        }
      }
      .product-image-uploader-icon {
        font-size: 18px;
        color: #8c939d;
        width: 80px;
        height: 80px;
        line-height: 80px;
        text-align: center;
      }
      .product-image {
        width: 80px;
        height: 80px;
        display: block;
      }
    }
  }
}
</style>
