import { Link, useLocation } from "react-router-dom";

const Sidebar = () => {

    const location = useLocation(); // Untuk tahu URL aktif yaww miww

    const isActive = (path) => location.pathname === path;

    return (
        <div className="w-60 bg-white text-black p-4 flex flex-col rounded-r-2xl justify-between">
            <div>
                <div className="flex justify-center mb-6 p-10">
                    <img src="icon/LoginIcon.webp" alt="logo" className="h-25 w-26" />
                </div>

                <section className="space-y-4 flex flex-col">

                    <Link to="/dashboard" className={`flex flex-row gap-5 ${isActive("/dashboard") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <img src="icon/home.png" className={`${isActive("/dashboard") ? "" : "grayscale"}`} />
                        <span>Home</span>
                    </Link>

                    <Link to="/mahasiswa" className={`flex flex-row gap-5 ${isActive("/mahasiswa") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <img src="icon/bachlor.png" className={`${isActive("/mahasiswa") ? "" : "grayscale"}`} />
                        <span>Data Mahasiswa</span>
                    </Link>

                    <Link to="/input" className={`flex flex-row gap-5 ${isActive("/input") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <img src="icon/input.png" className={`${isActive("/input") ? "" : "grayscale"}`} />
                        <span>Input & Evaluasi</span>
                    </Link>

                    <Link to="/statistik" className={`flex flex-row gap-5 ${isActive("/statistik") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <img src="icon/bar.png" className={`${isActive("/statistik") ? "" : "grayscale"}`} />
                        <span>Statistik Program Studi</span>
                    </Link>
                </section>
            </div>

            <div className="flex flex-row gap-5">
                <img src="icon/out.png" alt="" />
                <a href="#">Logout</a>
            </div>
        </div>
    )
}

export default Sidebar;