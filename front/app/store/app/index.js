export const state = () => ({
    felicaList: [],
    checkoutList: [],

    showDetailIndex: 0,
});

export const mutations = {
    setFelicaList(state, lists) {
        state.felicaList = lists;
    },
    setCheckoutList(state, lists) {
        state.checkoutList = lists
    },

    setDetailIndex(state, index) {
        state.showDetailIndex = index
    }
    
}

export const actions = {
    async getFelicaList({commit, rootState}){
        const response = await this.$axios({
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...rootState.auth
            },
            url: process.env.API_HOST + "/accounts/idm/"
        })
        .catch(err => {
            return false
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 200) {
            await commit("setFelicaList", response.data);
            return true
        } else {
            return false
        }
    },

    async getCheckoutList({state, commit, rootState}){
        const response = await this.$axios({
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...rootState.auth
            },
            url: process.env.API_HOST + "/accounts/checkouts/"
        })
        .catch(err => {
            return false
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 200) {
            await commit("setCheckoutList", response.data);
            return true
        } else {
            return false
        }
    },

}

export const getters = {
    getDetail(state) {
        return state.checkoutList[state.showDetailIndex];
    }
}