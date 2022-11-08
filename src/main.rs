use handlebars::Handlebars;
use std::fs;

fn main() {
    let mut handlebars = Handlebars::new();

    let template_path = "demo/template.hbs";
    let cv_toml = "demo/cv.toml";

    let template = fs::read_to_string(template_path).unwrap();
    assert!(handlebars
        .register_template_string("template", template)
        .is_ok());

    let contents = fs::read_to_string(cv_toml).unwrap();

    let data: toml::Value = toml::from_str(&contents).unwrap();

    // println!("{:?}", data);
    println!("{}", handlebars.render("template", &data).unwrap());
}
