export const state = () => ({
    auth: {
        "access-token": null,
        "client": null,
        "uid": null
    },
    menus: [
        // 10001~10100 = about userdatas
        {
            id: 10001,
            title: "ユーザ一覧",
            description: "利用者の一覧を表示します",
            authority: ["admin"],
            page: null,
        },
        {
            id: 10002,
            title: "ユーザ検索",
            description: "idm情報やldap名などを利用して、ユーザーを検索します",
            authority: ["admin"],
            page: null,
        },
        {
            id: 10011,
            title: "管理者権限承認",
            description: "管理者権限を付与します",
            authority: ["admin"],
            page: null,
        },
        {
            id: 10012,
            title: "管理者一覧",
            description: "管理者を表示します",
            authority: ["admin"],
            page: null,
        },
        // 10101~10200 = about payment datas
        {
            id: 10101,
            title: "電子ジャーナル照会",
            description: "T-Payで行われた決済の履歴を表示します",
            authority: ["admin"],
            page: null,
        },
        {
            id: 10102,
            title: "決済変更",
            description: "T-Payで行われた決済を変更します",
            authority: ["admin"],
            page: null,
        },
        // 10201~10300 = about money datas
        {
            id: 10201,
            title: "在高照会",
            description: "T-Pay上で管理されている在高を表示します",
            authority: ["admin"],
            page: null,
        },
        // 10301~10400 = about news
        {
            id: 10311,
            title: "一括メール送信",
            description: "利用者に向けたメールの一斉送信をします",
            authority: ["admin"],
            page: null,
        },

    ],
    sidemenus: [
        {
          title: "顧客管理",
          description: "",
          menus: [
            10001, 
          ]
        },
        {
          title: "権限管理",
          description: "",
          menus: []
        },
        {
          title: "決済管理",
          description: "",
          menus: []
        },
        {
          title: "金銭保守",
          description: "",
          menus: []
        },
        {
          title: "通知",
          description: "",
          menus: []
        }
    ],

    selectedSideMenuIndex: 0,

});

export const mutations = {
    setAuth(state, {access_token, client, uid}){
        state.auth = {
            "access-token": access_token,
            client: client,
            uid: uid
        }
    },
    setSideMenuIndex(state, index) {
        state.selectedSideMenuIndex = index;
    }
}

export const actions = {
    /**
     * POS起動時に実行. 
     */
    async initialize({ commit }) {
        const response = await this.$axios({
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*"
            },
            data: {
                email: process.env.POS_AUTH_EMAIL,
                password: process.env.POS_AUTH_PASSWORD
            },
            url: process.env.POS_HOST + "api/v1/auth/sign_in"
        })
        .catch(err => {
            return false
        });

        // 正常に通信が完了し、なおかつPOS権限を持っている場合
        if (response.status == 200 && response.data.data.authority_id == 2) {
            await commit("setAuth", {
                access_token: response.headers["access-token"],
                client: response.headers["client"],
                uid: response.headers["uid"]
            });
            return true
        } else {
            return false
        }

    },
    /**
     * 権限一覧の取得
     */
    async getAuthorities({commit, state}) {
        const response = await this.$axios({
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...state.auth
            },
            url: process.env.POS_HOST +"api/v1/authorities",
            timeout: 1000
        })
        .catch(err => {
            return false
        });

        if (response.status == 200) {
            commit("setAuthorities", response.data)
            return true
        } else {
            return false
        }
    },
    async getProducts({ commit, state }) {
        const response = await this.$axios({
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Access-Control-Allow-Origin": "*",
                ...state.auth
            },
            url: process.env.POS_HOST +"api/v1/products",
            timeout: 3000
        })
        .catch(err => {
            return false
        });

        if (response.status == 200) {
            commit("setProducts", response.data)
            return true
        } else {
            return false
        }
    }
}

export const getters = {
    selectedSideMenu (state) {
        return state.sidemenus[state.selectedSideMenuIndex];
    },
    menusList (state) {
        return state.menus.filter((menu, index) => {
            return (state.sidemenus[state.selectedSideMenuIndex].menus.includes(menu.id));
        });
    }
}