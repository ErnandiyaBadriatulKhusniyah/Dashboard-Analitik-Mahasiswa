export class EncryptedLocalStorage {
    constructor() {
        // Di sini akan ada logika enkripsi/dekripsi
        // Untuk contoh ini, kita akan membuat versi sederhananya
        this.key = 'super-secret-key'; // Kunci untuk enkripsi/dekripsi
    }

    // Metode untuk mengenkripsi data sebelum disimpan
    setItem(name, value) {
        try {
            const encryptedValue = btoa(JSON.stringify(value)); // Enkripsi sederhana pakai Base64
            localStorage.setItem(name, encryptedValue);
        } catch (e) {
            console.error("Error encrypting data for", name, e);
        }
    }

    // Metode untuk mendekripsi data saat diambil
    getItem(name) {
        try {
            const encryptedValue = localStorage.getItem(name);
            if (encryptedValue) {
                return JSON.parse(atob(encryptedValue)); // Dekripsi Base64
            }
            return null;
        } catch (e) {
            console.error("Error decrypting data for", name, e);
            return null; // Return null jika ada error dekripsi
        }
    }

    removeItem(name) {
        localStorage.removeItem(name);
    }
}