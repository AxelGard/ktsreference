

# foldTo

Groups elements from the Grouping source by key and applies operation to the elements of each group sequentially, passing the previously accumulated value and the current element as arguments, and stores the results in the given destination map. An initial value of accumulator is provided by initialValueSelector function.

```kotlin
inline fun <T, K, R, M : MutableMap<in K, R>> Grouping<T, K>.foldTo(destination: M, initialValueSelector: (key: K, element: T) -> R, operation: (key: K, accumulator: R, element: T) -> R): M(source)
```

```kotlin
import kotlin.collections.*

data class Person(val city: String, val age: Int)

val people = listOf(
    Person("NY", 25),
    Person("NY", 30),
    Person("LA", 22),
    Person("LA", 28),
    Person("LA", 35)
)

val ageSumByCity = mutableMapOf<String, Int>()

people
    .groupingBy { it.city }
    .foldTo(
        destination = ageSumByCity,
        initialValueSelector = { _, person -> person.age },
        operation = { _, acc, person -> acc + person.age }
    )

println(ageSumByCity)   // {NY=55, LA=85}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/fold-to.html)

    