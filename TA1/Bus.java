package TA1;//import vehicle.TA1.Driveble;
//import vehicle.TA1.PublicTransfer;

import java.awt.geom.Point2D;

public class Bus extends MotorVehicle implements Driveble, PublicTransfer {

    private static  final double busDelay = 0.3;
    private static final int minSeats = 20;
    private static final int speedLimit = 120;
    private int currPassengerCount;
    private Point2D pos;

    public Bus(String manufacturer, String model, String registrationPlate, int weight, int maxSpeed, int seats) {
        super(manufacturer, model, registrationPlate, weight, maxSpeed, seats);
        //if(seats< minSeats) throw new Exception("TA1.Bus must have at least 20"); //hard coded not good
        if(seats< minSeats) throw new RuntimeException("TA1.Bus must have at least "+minSeats+" seats but , You used only "+seats);
        this.currPassengerCount =0;
    }

    @Override
    public void setMaxSpeed(int maxSpeed) {
        int constrainedMaxSpeed = Math.min(maxSpeed, speedLimit);
    }

    @Override
    public int getMaxSpeed(){
        //return this.getMaxSpeed(); //-> stack overflow
        return super.getMaxSpeed();
    }

    @Override
    public void initPos(Point2D p) {
        this.pos = p;
    }

    @Override
    public Point2D getPos() {
        return pos;
    }

    @Override
    public double drive( Point2D dst) {
        if (pos ==null){
            System.out.println("you must firs init the pos ! ");
            throw new NullPointerException();}
        double distance = Point2D.distance(pos.getX(), pos.getY(), dst.getX(), dst.getY());
        double timeToTravel = distance/(getMaxSpeed()*busDelay);
        return timeToTravel;
    }

    @Override
    public int getCurrPassengerCount() {
    return  currPassengerCount;
    }

    @Override
    public void addPassenger() {
        currPassengerCount++;
    }

    @Override
    public void getOffPassenger() {
    currPassengerCount--;
    }

}