<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-button modifier="quiet" @click="popPage">キャンセル</v-ons-button>
      </div>
      <div class="center">パスワード変更</div>
    </v-ons-toolbar>

    <div>
      <el-input placeholder="Please input password" v-model="input11" show-password></el-input>
    </div>
  </v-ons-page>
</template>

<script>
export default {
  data() {
    return {
      input11
    };
  },
  methods: {
    popPage() {
      this.$emit("pop-page");
    }
  }
};
</script>

