export const state = () => ({
    felicaList: [],
    transactionList:[],

    showDetailIndex: 0,
});

export const mutations = {
    setFelicaList(state, lists) {
        state.felicaList = lists;
    },
    setTransactionList(state, lists) {
        if (lists.length > 0) {
            lists = lists.reverse();
            lists.forEach((item, index) => {
                item.index = index
            });
        }
        state.transactionList = lists
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
            url: process.env.API_HOST + "/accounts/idms/"
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

    async getTransaction({commit, rootState}) {
        const response = await this.$axios({
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...rootState.auth
            },
            url: process.env.API_HOST + "/transactions/"
        })
        .catch(err => {
            return false
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 200) {
            await commit("setTransactionList", response.data);
            return true
        } else {
            return false
        }
    },

    async deleteFelicaCard({dispatch, rootState}, id) {
        const response = await this.$axios({
            method: "DELETE",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...rootState.auth
            },
            url: process.env.API_HOST + "/accounts/idms/" + id
        })
        .catch(err => {
            return false
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 204) {
            await dispatch("getFelicaList");
            return true
        } else {
            return false
        }
    }

}

export const getters = {
    checkoutList(state) {
        return state.transactionList.filter(( value ) => {
            return value.type == "checkout";
        })
    },
    getDetail(state) {
        return state.transactionList[state.showDetailIndex];
    },

}