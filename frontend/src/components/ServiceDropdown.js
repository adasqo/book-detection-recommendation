import "../index.css"

const ServiceDropdown = (props) => {

    const handleSelect = (e) => {
        props.setLang(e.target.value);
      };

    return (
        <div>
            <p>Choose information provider</p>
            <select className="serviceDropdown" onChange={handleSelect}>
              <option value="pl">lubimyczytac.pl [PL]</option>
              <option value="eng">goodreads.com [ENG]</option>
            </select>
        </div>

    );
};

export default ServiceDropdown;