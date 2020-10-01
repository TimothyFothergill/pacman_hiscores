resource "aws_lb" "test" {
  name               = "pacman-alb-tf"
  internal           = true
  load_balancer_type = "application"
//  security_groups    = [aws_security_group.lb_sg.id]
//  subnets            = [aws_subnet.public.*.id]

  access_logs {
    bucket  = aws_s3_bucket.lb_logs.bucket
    prefix  = "pacman-lb"
    enabled = true
  }

  tags = {
    Environment = "development"
  }
}