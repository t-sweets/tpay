<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-button modifier="quiet" @click="popBack">キャンセル</v-ons-button>
      </div>
      <div class="center">送金</div>
    </v-ons-toolbar>

    <el-form
      ref="form"
      :model="form"
      label-position="top"
      label-width="10px"
      @submit.native.prevent="exec"
    >
      <el-form-item label="送金先">
        <el-input type="text" v-model="form.user_to_id"></el-input>
      </el-form-item>
      <el-form-item label="金額">
        <el-input-number :min="1" v-model="form.amount"></el-input-number>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" native-type="submit">送金する</el-button>
      </el-form-item>
    </el-form>

  </v-ons-page>



</template>

<script>
  import {mapActions} from 'vuex'
    export default {
    data(){
      return {
        form: {
          user_to_id: null,
          amount: 0
        }
      }
    },
      methods: {
        popBack() {
          this.$emit('pop-page')
        },
        exec() {
          this.transfer({
            user_to_id: this.form.user_to_id,
            amount: this.form.amount,
          })
        },
        ...mapActions("app/transfer", ["transfer"])
      }
    }
</script>

<style lang="scss" scoped>
form {
  @include pc {
    margin: 20px 50px;
  }
  @include sp {
    margin: 0;
  }
}
</style>
