import { Link, useLocation } from "react-router-dom";

import IconSI from "../../assets/icon/Prodi.png";
import { House } from 'lucide-react';
import { GraduationCap } from 'lucide-react';
import { FileCheck } from 'lucide-react';
import { ChartNoAxesColumn } from 'lucide-react';
import { LogOut } from 'lucide-react';

const Sidebar = () => {

    const location = useLocation(); // Untuk tahu URL aktif yaww miww

    const isActive = (path) => location.pathname === path;

    return (
        <div className="w-60 bg-white text-black p-4 flex flex-col rounded-r-2xl justify-between">
            <div>
                <div className="flex justify-center mb-6 p-10">
                    <img src={IconSI} alt="logo" className="h-17 w-23" />
                </div>

                <section className="space-y-4 flex flex-col">

                    <Link to="/dashboard" className={`flex flex-row gap-5 ${isActive("/dashboard") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <House />
                        <span>Home</span>
                    </Link>

                    <Link to="/mahasiswa" className={`flex flex-row gap-5 ${isActive("/mahasiswa") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <GraduationCap />
                        <span>Data Mahasiswa</span>
                    </Link>

                    <Link to="/input" className={`flex flex-row gap-5 ${isActive("/input") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <FileCheck />
                        <span>Input & Evaluasi</span>
                    </Link>

                    <Link to="/statistik" className={`flex flex-row gap-5 ${isActive("/statistik") ? "text-[#1D0080] font-bold" : "text-gray-400"}`}>
                        <ChartNoAxesColumn />
                        <span>Statistik Program Studi</span>
                    </Link>
                </section>
            </div>

            <div className="flex flex-row gap-5 text-[#1D0080] font-bold ">
                <LogOut />
                <a href="#">Logout</a>
            </div>
        </div>
    )
}

export default Sidebar;