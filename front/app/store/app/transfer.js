export const state = () => ({

});

export const mutations = {

}

export const actions = {
  async transfer({state, rootState}, {user_to_id, amount, message}){
    const response = await this.$axios({
      method: "POST",
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "*",
        ...rootState.auth
      },
      url: process.env.API_HOST + "/transfer/",
      data: {
        user_to_id: user_to_id,
        amount: amount,
        message: message
      }
    })
      .catch(err => {
        return err.response
      });

    // 正常に通信が完了した場合
    if (response.status == 201) {
      return true
    } else if (response.status == 400) {
      return response.data;
    } else {
      return null
    }
  }
}
