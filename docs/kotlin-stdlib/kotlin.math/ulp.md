

# ulp

Returns the ulp (unit in the last place) of this value.

```kotlin
expect val Double.ulp: Double(source)
```

```kotlin
import kotlin.math.ulp

fun main() {
    val number = 1.0
    val ulpValue = number.ulp
    println("ULP of $number is $ulpValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/ulp.html)

    