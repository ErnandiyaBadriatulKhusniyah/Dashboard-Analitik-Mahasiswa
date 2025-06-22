
import { create } from "zustand"
import { persist } from "zustand/middleware"
import { EncryptedLocalStorage } from "../../utils/encryption.util"

const initialState = {
    loginData: null
}

export const useLoginStore = create(
    persist(
        set => ({
            ...initialState,

            setLoginData: (loginData) => set({ loginData })
        }),
        {
            name: 'login-store',
            storage: new EncryptedLocalStorage()
        }
    )
)