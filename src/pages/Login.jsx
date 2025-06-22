import { useState } from "react";
import Input from "../components/atoms/Input"
import Icon from "../assets/icon/Prodi.svg";

const Login = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    const [formErrors, setFormErrors] = useState({});
    const [generalError, setGeneralError] = useState('');

    // 2. Handler perubahan tunggal untuk semua input
    const handleInputChange = (e) => {
        const { id, value } = e.target;
        setFormData(prevData => ({
            ...prevData,
            [id]: value,
        }));

        // Hapus error spesifik field saat input berubah
        if (formErrors[id]) {
            setFormErrors(prevErrors => {
                const newErrors = { ...prevErrors };
                delete newErrors[id]; // Hapus error untuk field yang sedang diubah
                return newErrors;
            });
        }
        // Hapus error umum saat ada input yang berubah
        if (generalError) {
            setGeneralError('');
        }
    };

    const validateForm = () => {
        let errors = {};
        let isValid = true;

        if (!formData.username.trim()) { // .trim() untuk mengabaikan spasi kosong
            errors.username = 'Username wajib diisi.';
            isValid = false;
        }

        if (!formData.password.trim()) {
            errors.password = 'Password wajib diisi.';
            isValid = false;
        } else if (formData.password.length < 6) {
            errors.password = 'Password minimal 6 karakter.';
            isValid = false;
        }

        setFormErrors(errors); // Update state error
        return isValid;
    };

    // 3. Handler untuk submit form
    const handleSubmit = (e) => {
        e.preventDefault();

        // Panggil fungsi validasi
        if (validateForm()) {
            // Jika validasi lokal lolos, lakukan sesuatu (misal: kirim ke API)
            console.log('Login attempt with:', formData);

            // Simulasi API call:
            if (formData.username === 'user' && formData.password === 'password123') {
                alert('Login berhasil!');
                // Reset form setelah submit berhasil
                setFormData({
                    username: '',
                    password: '',
                });
                setFormErrors({});
                setGeneralError('');
            } else {
                setGeneralError('Username atau password salah. Mohon periksa kembali.');
            }
        } else {
            setGeneralError('Ada kesalahan dalam pengisian form. Mohon periksa kembali.');
        }
    };

    return (
        <main className="max-h-screen h-screen w-full grid grid-cols-2">
            <div className="flex flex-col items-center justify-center p-8 gap-12">
                <img src={Icon} alt="icon-login" className="h-30 w-35" />
                <form onSubmit={handleSubmit} className="w-full max-w-sm">
                    <div className="mb-4">
                        <Input
                            id="username"
                            type="text"
                            value={formData.username}
                            onChange={handleInputChange}
                            placeholder="Username"
                            error={formErrors.username}
                            className="border-0 rounded-[20px] ring-1 ring-inset ring-[#A3AED0] focus:ring-2 focus:ring-[#9e8edc] focus:ring-inset block focus:outline-none"
                        />
                    </div>

                    <div className="mb-6">
                        <Input
                            id="password"
                            type="password"
                            value={formData.password}
                            onChange={handleInputChange}
                            placeholder="Password"
                            error={formErrors.password}
                            className="border-0 rounded-[20px] ring-1 ring-inset ring-[#A3AED0] focus:ring-2 focus:ring-[#9e8edc] focus:ring-inset block focus:outline-none"
                        />
                    </div>

                    {generalError && <p className="text-red-500 text-sm mb-4 text-center">{generalError}</p>}

                    <button
                        type="submit"
                        className="w-full bg-[#2A0E99] text-white py-2 px-4 rounded-md hover:bg-opacity-90 transition-colors"
                    >
                        Login
                    </button>
                </form>
            </div>

            <aside className="bg-[#2A0E99] rounded-l-2xl flex items-center px-30">
                <div className="flex flex-col gap-2">
                    <span className="text-white text-[40px]">Welcome to !</span>
                    <div>
                        <h1 className="text-[80px]/22 text-white font-medium">Dashboard Analitik </h1>
                    </div>
                </div>
            </aside>
        </main>
    )
}

export default Login;