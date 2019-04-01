export const state = () => ({
    auth: {
        "Authorization": null,
    },
    profile: {
        username: null,
        email: null,
        display_name: null,
        balance: 0,
        icon: {
            image: null
        }
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
            balance: profile.balance,
            icon: profile.icon
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
            return err.response
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
            return err.response
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 200 && response.data.token) {
            await commit("setAuth", `token ${response.data.token}`);
            return true
        } else if (response.status == 400) {
            return response.data
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
            return err.response
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 200) {
            await commit("setProfile", response.data);
            return true
        } else if (response.status == 400) {
            return response.data.non_field_errors
        } else {
            return false
        }
    },

    async updateProfile({state, commit}, {display_name, email, icon_id}) {
        const response = await this.$axios({
            method: "PATCH",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...state.auth
            },
            data: {
                display_name: display_name,
                email: email,
                icon: icon_id
            },
            url: process.env.API_HOST + "/accounts/profile/"
        }).catch(err => {
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

    async uploadIcon({state, dispatch, commit}, formdata) {
        const response = await this.$axios({
            method: "POST",
            headers: {
                "Content-Type": "multipart/form-data;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...state.auth
            },
            data: formdata,
            url: process.env.API_HOST + "/media/upload/"
        }).catch(err => {
            return err.response
        });

        // 正常に通信が完了し、なおかつtokenを持っている場合
        if (response.status == 201) {
            await dispatch("updateProfile", {icon_id: response.data.id})
            return true
        } else {
            return false
        }
    }
}
