import './Header.css';
import mainLogo from '../../images/main-logo.png';

function Header() {
  return (
    <div className="header-container">
      <img className="header-logo" src={ mainLogo } alt="mainLogo" />
      <div className="header">
        <div className="title">
          BCI_GUI
        </div>
      </div>
    </div>
  );
}

export default Header;