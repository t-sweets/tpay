export const state = () => ({
    auth: {
        "Authorization": null,
    },
    profile: {
        username: null,
        email: null,
        display_name: null,
        balance: 0
    }
});

export const mutations = {
    setAuth(state, token){
        state.auth = {
            "Authorization": token
        }
    },
    setProfile(state, profile) {
        state.profile = {
            username: profile.username,
            email: profile.email,
            display_name: profile.display_name,
            balance: profile.balance
        }
    }
}

export const actions = {
    async register({commit}, {username, email, display_name, password}){
        const response = await this.$axios({
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*"
            },
            data: {
                username: username,
                email: email,
                display_name: display_name,
                password: password
            },
            url: process.env.API_HOST + "/accounts/register/"
        })
        .catch(err => {
            return false
        });

        if (response.status == 201) {
            return true
        } else {
            return false
        }
    },

    async login({commit}, {username, password}){
        const response = await this.$axios({
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*"
            },
            data: {
                username: username,
                password: password
            },
            url: process.env.API_HOST + "/accounts/login/"
        })
        .catch(err => {
            return false
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 200 && response.data.token) {
            await commit("setAuth", `token ${response.data.token}`);
            return true
        } else {
            return false
        }
    },

    async getProfile({state, commit}){
        const response = await this.$axios({
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...state.auth
            },
            url: process.env.API_HOST + "/accounts/profile/"
        })
        .catch(err => {
            return false
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 200) {
            await commit("setProfile", response.data);
            return true
        } else {
            return false
        }
    },


}