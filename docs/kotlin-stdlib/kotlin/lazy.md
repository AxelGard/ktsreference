

# lazy

Creates a new instance of the Lazy that uses the specified initialization function initializer and the default thread-safety mode LazyThreadSafetyMode.SYNCHRONIZED. The lock used is both platform- and implementation- specific detail.

```kotlin
expect fun <T> lazy(initializer: () -> T): Lazy<T>(source)
```

```kotlin
class Example {
    val expensiveValue: Lazy<Int> = lazy {
        println("Computing value")
        42
    }
}

fun main() {
    val ex = Example()
    println(ex.expensiveValue.value)   // prints "Computing value" and then 42
    println(ex.expensiveValue.value)   // prints 42 (no recomputation)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/lazy.html)

    