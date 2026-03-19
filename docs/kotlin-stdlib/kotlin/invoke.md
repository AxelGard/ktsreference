

# invoke

Initiates a call to this deep recursive function, forming a root of the call tree.

```kotlin
operator fun <T, R> DeepRecursiveFunction<T, R>.invoke(value: T): R(source)
```

```kotlin
import kotlin.core.*

fun main() {
    // Define a deep‑recursive factorial function
    val factorial = deepRecursiveFunction<Int, Long> { n ->
        if (n <= 1) 1L else n * this(n - 1)   // `this` refers to the DeepRecursiveFunction instance
    }

    // Invoke the function using the operator syntax
    println(factorial(5))   // prints 120
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/invoke.html)

    