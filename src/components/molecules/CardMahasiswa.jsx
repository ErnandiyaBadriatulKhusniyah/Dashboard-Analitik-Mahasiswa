import { Link } from "react-router-dom";

const CardMahasiswa = ({ icon, jumlah, label, to, }) => {
    return (

        <Link to={to}>
            <div className="bg-white p-4 rounded-xl shadow-md w-[350px] h-[142px] flex gap-10 items-center justify-between cursor-pointer hover:shadow-lg transition">
                <img src={icon} alt="icon" />
                <div className="flex flex-col text-end">
                    <p className="text-[50px] font-bold">{jumlah}</p>
                    <p className="text-md font-medium">{label}</p>

                </div>
            </div>
        </Link>

    );
};

export default CardMahasiswa; 