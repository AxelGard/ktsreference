

# withSign

Returns this value with the sign bit same as of the sign value.

```kotlin
expect fun Double.withSign(sign: Double): Double(source)
```

```kotlin
fun main() {
    val value   = 5.0          // magnitude to preserve
    val signNeg = -3.0         // negative sign source
    val signPos = 4.0          // positive sign source

    println("value with negative sign: ${value.withSign(signNeg)}") // -5.0
    println("value with positive sign: ${value.withSign(signPos)}") // 5.0

    println("-8.0 with positive sign: ${(-8.0).withSign(signPos)}") // 8.0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/with-sign.html)

    