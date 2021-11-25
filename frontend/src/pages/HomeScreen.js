import { Layout } from '../components/layout/Layout';
import { image } from "../helpers/image";

export const HomeScreen = () => {
    return (
        <Layout>  
            <div className="contenido">
                <div className="botonera">
                    <div>
                        <button className="btn btn-secondary"></button>
                        <button className="btn btn-secondary"></button>
                    </div>
                    <div>
                        <button className="btn btn-secondary"></button>
                        <button className="btn btn-secondary"></button>
                    </div>
                </div>
                <img
                    className="calendario"
                    src={ image('./calendario.jpg').default }
                    alt="calendario"
                ></img>
            </div>
        </Layout>
    )
};
