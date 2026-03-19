

# ceil

Rounds the given value x to an integer towards positive infinity.

```kotlin
expect fun ceil(x: Double): Double(source)
```

```kotlin
import kotlin.math.ceil

fun main() {
    val number = 3.14
    val rounded = ceil(number)
    println("Ceiling of $number is $rounded") // 4.0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/ceil.html)

    