export const state = () => ({
    idm: null
});

export const mutations = {
    setIdm(state, idm) {
        state.idm = idm;
    },
    resetIdm(state) {
        state.idm = null;
    }
}

export const actions = {
    async registerIdm({state, rootState}, {name, image_id}){
        const response = await this.$axios({
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...rootState.auth
            },
            url: process.env.API_HOST + "/accounts/idms/",
            data: {
                idm: state.idm,
                name: name
            }
        })
        .catch(err => {
            return err.response
        });

        // 正常に通信が完了した場合
        if (response.status == 201) {
            return true
        } else if (response.status == 400 && response.data.idm) {
            return response.data.idm;
        } else {
            return null
        }
    }
}
