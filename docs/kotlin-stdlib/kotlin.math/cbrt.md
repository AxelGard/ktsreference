

# cbrt

Returns the cube root of x. For any x, cbrt(-x) == -cbrt(x); that is, the cube root of a negative value is the negative of the cube root of that value's magnitude.

```kotlin
expect fun cbrt(x: Double): Double(source)
```

```kotlin
import kotlin.math.cbrt

fun main() {
    val number = 27.0
    val cubeRoot = cbrt(number)
    println("Cube root of $number is $cubeRoot")

    val negativeNumber = -8.0
    val negativeCubeRoot = cbrt(negativeNumber)
    println("Cube root of $negativeNumber is $negativeCubeRoot")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/cbrt.html)

    