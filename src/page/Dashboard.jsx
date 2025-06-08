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
const data = {
    labels: matakuliah.map(item => item.mk),
    datasets: [{
        data: matakuliah.map(item => item.total_mahasiswa),
        backgroundColor: [
            '#7893FF',
            '#573BD4',
            '#2B4386',
            '#7887B9',
            '#A79BD7',
        ]
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
            position: 'left',
            align: 'center',
        },
    },
}

const Dashboard = () => {
    return (
        <main className="h-screen w-full">
            <Layout className="flex flex-col gap-10 ">
                <HeaderDashboard />
                <section className="bg-white rounded-lg py-4 px-10 space-y-5">
                    <Typography variantClass="h1" className="font-bold text-center text-2xl">Top Matakuliah Pilihan Mahasiswa</Typography>
                    <div className="grid grid-cols-[50%_50%] justify-center">
                        <div className="">
                            <Doughnut options={options} className="max-h-[300px] max-w-fit" data={data} />
                        </div>
                        <div className="flex flex-col gap-2">
                            <div className="bg-[#F2F2F2] grid grid-cols-2 text-center p-1 rounded-md shadow">
                                <Typography variantClass="h4">
                                    Mata Kuliah
                                </Typography>
                                <Typography variantClass="h4">
                                    Total Mahasiswa
                                </Typography>
                            </div>
                            <div>
                                {matakuliah.map((item, index) => (
                                    <div key={index} className="grid grid-cols-2 text-center p-1 rounded-md ">
                                        <Typography variantClass="p" className="text-black">
                                            {item.mk}
                                        </Typography>
                                        <Typography variantClass="p">
                                            {item.total_mahasiswa}
                                        </Typography>
                                    </div>
                                ))}
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