mod args;

use args::Args;
use clap::Parser;
use handlebars::Handlebars;
use std::fs;

fn main() {
    let args = Args::parse();

    let mut handlebars = Handlebars::new();

    let template_path = format!("{}/{}", args.folder, args.template);
    let data_path = format!("{}/{}", args.folder, args.cv);
    let output_path = format!("{}/{}", args.folder, args.output);

    let template = fs::read_to_string(template_path)
        .unwrap_or_else(|_| panic!("Could not read template file {}", args.template));

    handlebars
        .register_template_string("template", template)
        .expect("Unable to register template");

    let contents = fs::read_to_string(data_path)
        .unwrap_or_else(|_| panic!("Could not read cv data file {}", args.cv));

    let mut data: toml::Value = toml::from_str(&contents).expect("Unable to parse cv data");

    data.as_table_mut()
        .unwrap()
        .insert("media".to_string(), toml::Value::String(args.media));

    let rendered = handlebars
        .render("template", &data)
        .expect("Unable to render output");

    fs::write(output_path, rendered).expect("Unable to write file");

    println!("CV successfully generated! Seize the day!");
}
