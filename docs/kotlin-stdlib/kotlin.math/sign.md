

# sign

Returns the sign of the given value x:

```kotlin
expect fun sign(x: Double): Double(source)
```

```kotlin
import kotlin.math.sign

fun main() {
    val values = listOf(-3.5, 0.0, 4.2)

    values.forEach { v ->
        println("sign($v) = ${sign(v)}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/sign.html)

    