# satellite-pix2pix
An image to image translation project. 

# Idea

As stated in the paper [Image-to-Image Translation with Conditional Adversarial Networks
](https://arxiv.org/pdf/1611.07004.pdf) pix2pix approach is used to develop a network which learns a mapping from input 
to an output image. Along with that the stated network also learns a loss function required for the stated mapping. 
In effect getting rid of the need to frame loss function for each of these mappings/translation tasks, which otherwise
would require very distinct loss functions. 

Some examples of such translations as presented in the original paper can be seen below:

![ example of image to image translation](https://phillipi.github.io/pix2pix/images/teaser_v3.jpg)

Several research papers have worked on image to image translation using GANs, however, mostly all of them were not
conditioning the output given the input, mostly relying on penalty terms such as ('L2') penalty in regression for 
conditioning output on the input. This approach uses conditioning and is not application specific. A general
image to image translation. There are also some architectural specific changes when compared to the prior work, for
example, use of [U-Net](https://arxiv.org/abs/1505.04597) based architecture for generator and a PatchGAN classifier
as discriminator. 


