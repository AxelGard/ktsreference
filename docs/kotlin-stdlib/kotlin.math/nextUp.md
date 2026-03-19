

# nextUp

Returns the Double value nearest to this value in direction of positive infinity.

```kotlin
expect fun Double.nextUp(): Double(source)
```

```kotlin
fun main() {
    val value = 2.5
    val next = value.nextUp()
    println("The next representable double after $value is $next")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/next-up.html)

    