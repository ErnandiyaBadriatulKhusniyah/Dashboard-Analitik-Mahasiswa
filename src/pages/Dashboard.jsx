import Typography from "../components/atoms/Typograpy";
import HeaderDashboard from "../components/molecules/HeaderDashboard";
import Layout from "../components/templates/Layout";
import { ArcElement, Chart, Legend, Title, Tooltip } from "chart.js";
import { Doughnut } from 'react-chartjs-2';

Chart.register(ArcElement, Tooltip, Legend, Title)

const matakuliah = [
    {
        mk: 'E-Business',
        total_mahasiswa: 10
    },
    {
        mk: 'TKTI',
        total_mahasiswa: 10
    },
    {
        mk: 'Statprob',
        total_mahasiswa: 10
    },
    {
        mk: 'Intelejen Bisnis',
        total_mahasiswa: 10
    },
    {
        mk: 'Visualisasi Data',
        total_mahasiswa: 10
    },

];
const chartColors = [
    '#7893FF',
    '#573BD4',
    '#2B4386',
    '#7887B9',
    '#A79BD7',
];
const data = {
    labels: matakuliah.map(item => item.mk),
    datasets: [{
        data: matakuliah.map(item => item.total_mahasiswa),
        backgroundColor: chartColors
    }],
};

export const options = {
    responsive: true,

    plugins: {
        title: {
            display: true,
            text: 'Top 5 Matakuliah',
            font: {
                size: 15
            },
            position: 'top',
            align: 'start'
        },
        legend: { // Atur posisi legend jika perlu
            position: 'bottom',
            align: 'center',
        },
    },
}

const Dashboard = () => {
    return (
        <main className="h-screen w-full">
            <Layout className="flex flex-col gap-10 ">
                <HeaderDashboard children={"Dashboard"} />
<<<<<<< HEAD:src/page/Dashboard.jsx
                <section className="bg-white rounded-lg py-4 px-10 space-y-5">
                    <Typography variantClass="h1" className="font-bold text-center text-2xl">Top Matakuliah Pilihan Mahasiswa</Typography>
                     <div className="grid grid-cols-[50%_50%] justify-center">
                        <div className="">
=======
                <section className=" space-y-5">
                    <div className="justify-center grid grid-cols-[50%_50%] space-x-5">
                        <div className="bg-white rounded-lg py-4 px-10">
>>>>>>> 065d2e40513a86f4af7422bb9b685c3f93bd2708:src/pages/Dashboard.jsx
                            <Doughnut options={options} className="max-h-[300px] max-w-fit" data={data} />
                        </div>
                        <div className="flex flex-col gap-2 bg-white rounded-lg py-4 px-10">
                            <div className="grid grid-cols-2 pl-4">
                                <Typography variantClass="h4" className={'font-semibold'}>
                                    Mata Kuliah
                                </Typography>
                                <Typography variantClass="h4" className={'font-semibold'}>
                                    Total Mahasiswa
                                </Typography>
                            </div>
                            <div className="">
                                {matakuliah.map((item, index) => {
                                    const borderColor = chartColors[index % chartColors.length];
                                    return (
                                        <div key={index} className={`grid grid-cols-2 border-b pl-4 py-3 border-t border-gray-200 border-l-4`}
                                            style={{ borderLeftColor: borderColor }}>
                                            <Typography variantClass="p" className="text-black">
                                                {item.mk}
                                            </Typography>
                                            <Typography variantClass="p">
                                                {item.total_mahasiswa}
                                            </Typography>
                                        </div>
                                    )
                                })}
                            </div>
                        </div>
                    </div>
                </section>
                <div className="bg-white rounded-lg">
                    chart
                </div>
            </Layout>
        </main>
    )
}

export default Dashboard;