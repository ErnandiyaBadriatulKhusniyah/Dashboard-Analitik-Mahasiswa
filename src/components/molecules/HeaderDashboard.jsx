import Typography from "../atoms/Typograpy";

const HeaderDashboard = () => {
    return (
        <div className="flex items-center justify-between bg-white p-4 rounded-lg">
            <Typography variantClass="h1" className="font-semibold">
                Home
            </Typography>
            <Typography>Hi, Miftahul Rizqha</Typography>
        </div>
    )
}

export default HeaderDashboard;