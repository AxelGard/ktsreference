

# sumBy

Warning since 1.5

```kotlin
inline fun <T> Array<out T>.sumBy(selector: (T) -> Int): Int(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val totalAge = people.sumBy { it.age }

println("Total age: $totalAge")  // Output: Total age: 90
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sum-by.html)

    