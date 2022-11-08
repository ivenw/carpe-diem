use clap::Parser;

#[derive(Parser, Debug)]
#[clap(about, version, author)]
pub struct Args {
    /// The folder to run carpe-diem from
    #[clap(short, long, default_value = ".")]
    pub folder: String,

    /// The template .hbs file to use
    #[clap(short, long, default_value = "template.hbs")]
    pub template: String,

    /// The cv data .toml file to use
    #[clap(short, long, default_value = "cv.toml")]
    pub cv: String,

    /// The media folder to use
    #[clap(short, long, default_value = "media")]
    pub media: String,

    /// The output file to use
    #[clap(short, long, default_value = "cv.html")]
    pub output: String,
}
